from .forms import PetitionSearchForm


def search_pet(request):
    return {
        'search_form': PetitionSearchForm()
    }
