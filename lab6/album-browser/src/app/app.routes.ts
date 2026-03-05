import { Routes } from '@angular/router';

export const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', loadComponent: () => import('./pages/home/home').then((m) => m.Home) },
  { path: 'about', loadComponent: () => import('./pages/about/about').then((m) => m.About) },
  { path: 'albums', loadComponent: () => import('./pages/albums/albums').then((m) => m.Albums) },
  {
    path: 'albums/:id',
    loadComponent: () => import('./pages/album-detail/album-detail').then((m) => m.AlbumDetail),
  },
  {
    path: 'albums/:id/photos',
    loadComponent: () => import('./pages/album-photos/album-photos').then((m) => m.AlbumPhotos),
  },
];
