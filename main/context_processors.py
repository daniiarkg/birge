from .forms import PetitionSearcForm


def search_pet(request):
    return {
        'search_form': PetitionSearchForm()
    }
