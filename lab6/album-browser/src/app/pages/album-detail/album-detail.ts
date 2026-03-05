import { Component, OnInit, signal } from '@angular/core';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';

import { Album } from '../../models/album.model';
import { AlbumService } from '../../services/album.service';

@Component({
  selector: 'app-album-detail',
  imports: [RouterLink, FormsModule],
  templateUrl: './album-detail.html',
  styleUrl: './album-detail.css',
})
export class AlbumDetail implements OnInit {
  album = signal<Album | null>(null);
  loading = signal(true);
  editTitle = signal('');
  saving = signal(false);

  constructor(
    private route: ActivatedRoute,
    private albumService: AlbumService,
  ) {}

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (!id) return;
    const numId = Number(id);
    if (Number.isNaN(numId)) {
      this.loading.set(false);
      return;
    }
    this.albumService.getAlbum(numId).subscribe({
      next: (data) => {
        this.album.set(data);
        this.editTitle.set(data.title);
        this.loading.set(false);
      },
      error: () => this.loading.set(false),
    });
  }

  onSave(): void {
    const a = this.album();
    if (!a) return;
    this.saving.set(true);
    const updated: Album = { ...a, title: this.editTitle() };
    this.albumService.updateAlbum(updated).subscribe({
      next: (data) => {
        this.album.set(data);
        this.editTitle.set(data.title);
        this.saving.set(false);
      },
      error: () => this.saving.set(false),
    });
  }
}
