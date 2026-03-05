import { Component, OnInit, signal } from '@angular/core';
import { RouterLink } from '@angular/router';

import { Album } from '../../models/album.model';
import { AlbumService } from '../../services/album.service';

@Component({
  selector: 'app-albums',
  imports: [RouterLink],
  templateUrl: './albums.html',
  styleUrl: './albums.css',
})
export class Albums implements OnInit {
  albums = signal<Album[]>([]);
  loading = signal(true);

  constructor(private albumService: AlbumService) {}

  ngOnInit(): void {
    this.albumService.getAlbums().subscribe({
      next: (data) => {
        this.albums.set(data);
        this.loading.set(false);
      },
      error: () => this.loading.set(false),
    });
  }

  onDelete(id: number, event: Event): void {
    event.preventDefault();
    event.stopPropagation();
    this.albumService.deleteAlbum(id).subscribe({
      next: () => {
        this.albums.update((list) => list.filter((a) => a.id !== id));
      },
    });
  }
}
