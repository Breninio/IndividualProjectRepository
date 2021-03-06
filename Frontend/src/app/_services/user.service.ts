import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { User } from 'src/app/_models/user';

@Injectable({ providedIn: 'root' })
export class UserService {
  constructor(private http: HttpClient) { }

  getAll() {
    return this.http.get<User[]>('http://127.0.0.1:5000/users');
  }

  register(user: User) {
    return this.http.post('http://127.0.0.1:5000/register', user);
  }

  delete(id: number) {
    return this.http.delete('http://127.0.0.1:5000/users/${id}');
  }
}
