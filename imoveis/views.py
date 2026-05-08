import json
from django.http import JsonResponse, Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Imovel, Imagem
from .forms import ImovelForm


class ImovelListView(ListView):
    model = Imovel
    template_name = 'imoveis/imovel_list.html'
    context_object_name = 'imoveis'


class ImovelDetailView(DetailView):
    model = Imovel
    template_name = 'imoveis/imovel_detail.html'
    context_object_name = 'imovel'


class ImovelCreateView(CreateView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'imoveis/imovel_form.html'
    success_url = reverse_lazy('imovel_list')

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)

            self.object.save()

            for imagem in self.request.FILES.getlist('outras_imagens'):
                Imagem.objects.create(
                    imovel=self.object,
                    imagem=imagem
                )

            return HttpResponseRedirect(self.get_success_url())

        except Exception as e:
            return HttpResponse(f"""
                <h1>ERRO AO SALVAR IMÓVEL</h1>
                <pre>{str(e)}</pre>
            """)


class ImovelUpdateView(UpdateView):
    model = Imovel
    form_class = ImovelForm
    template_name = 'imoveis/imovel_form.html'
    success_url = reverse_lazy('imovel_list')

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)

            self.object.save()

            for imagem in self.request.FILES.getlist('outras_imagens'):
                Imagem.objects.create(
                    imovel=self.object,
                    imagem=imagem
                )

            return HttpResponseRedirect(self.get_success_url())

        except Exception as e:
            return HttpResponse(f"""
                <h1>ERRO AO ATUALIZAR IMÓVEL</h1>
                <pre>{str(e)}</pre>
            """)


class ImovelDeleteView(DeleteView):
    model = Imovel
    template_name = 'imoveis/imovel_confirm_delete.html'
    success_url = reverse_lazy('imovel_list')


def delete_imagem(request, pk):
    imagem = get_object_or_404(Imagem, pk=pk)
    imovel_pk = imagem.imovel.pk

    if request.method == 'POST':
        imagem.delete()

    return redirect('imovel_update', pk=imovel_pk)


def _serialize_imovel(imovel, request):
    imagens = []

    for imagem in imovel.imagens.all():
        if imagem.imagem:
            imagens.append(
                request.build_absolute_uri(imagem.imagem.url)
            )

    if not imagens:
        if imovel.imagens.exists():
            imagens = [
                request.build_absolute_uri(
                    imovel.imagens.first().imagem.url
                )
            ]
        else:
            imagens = [
                request.build_absolute_uri('/imovel1.jpg')
            ]

    return {
        'id': imovel.id,
        'titulo': imovel.titulo,
        'descricao': imovel.descricao,
        'preco': float(imovel.preco),
        'cidade': imovel.cidade,
        'bairro': imovel.bairro,
        'quartos': imovel.quartos,
        'banheiros': imovel.banheiros,
        'vagas': imovel.vagas_garagem,
        'tipo_vaga': imovel.tipo_vaga,
        'tipo_vaga_display': imovel.get_tipo_vaga_display() if imovel.tipo_vaga else None,
        'metragem': float(imovel.metragem),
        'tipo': imovel.tipo,
        'finalidade': imovel.finalidade,
        'status': imovel.status,
        'imagem': imagens[0],
        'imagens': imagens,
        'previsao': getattr(imovel, 'previsao', ''),
        'situacao': getattr(imovel, 'situacao', imovel.status),
        'whatsapp': imovel.link_whatsapp() if hasattr(imovel, 'link_whatsapp') else None,
    }


@csrf_exempt
def api_imoveis_list(request):

    if request.method == 'OPTIONS':
        return JsonResponse({}, status=200)

    if request.method == 'GET':
        imoveis = Imovel.objects.all()

        data = [
            _serialize_imovel(imovel, request)
            for imovel in imoveis
        ]

        return JsonResponse(data, safe=False)

    if request.method == 'POST':

        try:
            payload = json.loads(
                request.body.decode('utf-8') or '{}'
            )

        except json.JSONDecodeError:
            return JsonResponse(
                {'error': 'JSON inválido'},
                status=400
            )

        imovel = Imovel.objects.create(
            titulo=payload.get('titulo', ''),
            descricao=payload.get('descricao', ''),
            preco=payload.get('preco', 0),
            cidade=payload.get('cidade', ''),
            bairro=payload.get('bairro', ''),
            quartos=payload.get('quartos', 0),
            banheiros=payload.get('banheiros', 0),
            vagas_garagem=payload.get('vagas', 0),
            tipo_vaga=payload.get('tipo_vaga'),
            metragem=payload.get('metragem', 0),
            tipo=payload.get('tipo', 'casa'),
            finalidade=payload.get('finalidade', 'venda'),
            status=payload.get('status', 'pronto'),
        )

        return JsonResponse(
            _serialize_imovel(imovel, request),
            status=201
        )

    return JsonResponse(
        {'error': 'Método não permitido'},
        status=405
    )


@csrf_exempt
def api_imovel_detail(request, pk):

    if request.method == 'OPTIONS':
        return JsonResponse({}, status=200)

    try:
        imovel = Imovel.objects.get(pk=pk)

    except Imovel.DoesNotExist:
        raise Http404('Imóvel não encontrado')

    if request.method == 'GET':
        return JsonResponse(
            _serialize_imovel(imovel, request)
        )

    if request.method == 'PUT':

        try:
            payload = json.loads(
                request.body.decode('utf-8') or '{}'
            )

        except json.JSONDecodeError:
            return JsonResponse(
                {'error': 'JSON inválido'},
                status=400
            )

        if payload.get('titulo') is not None:
            imovel.titulo = payload['titulo']

        if payload.get('descricao') is not None:
            imovel.descricao = payload['descricao']

        if payload.get('preco') is not None:
            imovel.preco = payload['preco']

        if payload.get('cidade') is not None:
            imovel.cidade = payload['cidade']

        if payload.get('bairro') is not None:
            imovel.bairro = payload['bairro']

        if payload.get('quartos') is not None:
            imovel.quartos = payload['quartos']

        if payload.get('banheiros') is not None:
            imovel.banheiros = payload['banheiros']

        if payload.get('vagas') is not None:
            imovel.vagas_garagem = payload['vagas']

        if payload.get('tipo_vaga') is not None:
            imovel.tipo_vaga = payload['tipo_vaga']

        if payload.get('metragem') is not None:
            imovel.metragem = payload['metragem']

        if payload.get('tipo') is not None:
            imovel.tipo = payload['tipo']

        if payload.get('finalidade') is not None:
            imovel.finalidade = payload['finalidade']

        if payload.get('status') is not None:
            imovel.status = payload['status']

        imovel.save()

        return JsonResponse(
            _serialize_imovel(imovel, request)
        )

    if request.method == 'DELETE':
        imovel.delete()

        return JsonResponse({'deleted': True})

    return JsonResponse(
        {'error': 'Método não permitido'},
        status=405
    )