import { Component, OnInit, signal } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';

import { Photo } from '../../models/photo.model';
import { AlbumService } from '../../services/album.service';

@Component({
  selector: 'app-album-photos',
  imports: [RouterLink],
  templateUrl: './album-photos.html',
  styleUrl: './album-photos.css',
})
export class AlbumPhotos implements OnInit {
  photos = signal<Photo[]>([]);
  loading = signal(true);
  albumId: number | null = null;

  constructor(
    private route: ActivatedRoute,
    private albumService: AlbumService,
  ) {}

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (!id) {
      this.loading.set(false);
      return;
    }
    const numId = Number(id);
    if (Number.isNaN(numId)) {
      this.loading.set(false);
      return;
    }
    this.albumId = numId;
    this.albumService.getAlbumPhotos(numId).subscribe({
      next: (data) => {
        this.photos.set(data);
        this.loading.set(false);
      },
      error: () => this.loading.set(false),
    });
  }
}
