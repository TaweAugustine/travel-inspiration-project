from django.urls import path

from .views import (
    HomeView,
    TravelInspirationView,
    TravelInspirationCreateView,
    TravelInspirationListView,
    FavoriteDetailView,
    FavoritesListView,
    TravelInspirationDetailView,
    CreateFavoriteView,
    TravelInspirationReSearchView,
    create_travel_inspiration,
)

app_name = "voyage_app"

urlpatterns = [
    # DEFAULT HOME
    path("",HomeView.as_view(),name="home"),

    # TRAVEL INSPIRATION ROUTE

    path("api/travel-inspiration-home/",TravelInspirationView.as_view(),name="travel-inspiration-home"),
    path("api/travel-inspiration-create/",create_travel_inspiration,name="travel-inspiration-create"),
    path("api/travel-inspiration/",TravelInspirationListView.as_view(),name="travel-inspiration-list"),
    path("api/travel-inspiration/<int:id>/",TravelInspirationDetailView.as_view(),name="travel-inspiration-detail"),
    path("api/travel-inspiration/search/",TravelInspirationReSearchView.as_view(),name='search-travel'),

    # FAVORITE ROUTE 
    path("api/travel-inspiration/favorites/",FavoritesListView.as_view(),name="favorite-list"),
    path("api/travel-inspiration/favorites/<int:id>/",FavoriteDetailView.as_view(),name="favorite-detail"),
    path("api/favorites/create/<int:id>/",CreateFavoriteView.as_view(),name="favorite-create"),
]