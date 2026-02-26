import { Component, Input } from '@angular/core';
import { ProductCard } from '../product-card/product-card';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-list',
  imports: [ProductCard],
  templateUrl: './product-list.html',
  styleUrl: './product-list.css',
})
export class ProductList {
  @Input({ required: true }) products: Product[] = [];

  handleDelete(productId: number): void {
    const index = this.products.findIndex((p) => p.id === productId);
    if (index !== -1) {
      this.products.splice(index, 1);
    }
  }

  get hasProducts(): boolean {
    return this.products.length > 0;
  }
}
