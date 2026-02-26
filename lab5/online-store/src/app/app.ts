import { Component } from '@angular/core';
import { ProductList } from './components/product-list/product-list';
import { Product } from './models/product.model';
import { Category } from './models/category.model';
import { PRODUCTS } from './data/products.data';
import { CATEGORIES } from './data/categories.data';

@Component({
  selector: 'app-root',
  imports: [ProductList],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  title = 'online-store';

  categories: Category[] = CATEGORIES;
  products: Product[] = PRODUCTS;

  selectedCategoryId: number | null = null;

  get selectedProducts(): Product[] {
    if (this.selectedCategoryId === null) {
      return [];
    }
    return this.products.filter(
      (product) => product.categoryId === this.selectedCategoryId,
    );
  }

  selectCategory(categoryId: number): void {
    this.selectedCategoryId = categoryId;
  }
}
