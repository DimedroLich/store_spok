from products.models import Basket


def basket(request):
    """Переменная basket вынесена глобально через файл settings.py и используется в шаблонах. До этого добавлялаьс в
    CBV через метод get_context_data"""
    user = request.user
    return {'basket': Basket.objects.filter(user=user) if user.is_authenticated else []}
