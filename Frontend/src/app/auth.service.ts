import { Injectable } from '@angular/core';
import { HttpHeaders } from '@angular/common/http';
import {HttpClient, HttpClientModule} from '@angular/common/http';
//import 'rxjs/add/operator/toPromise';

//@Injectable({
 // providedIn: 'root'
//})
@Injectable()
export class AuthService {
  //private BASE_URL: string = 'http://localhost:5000/auth';
  url = 'http://localhost:5000/auth/login';
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };
}
  /*constructor(private http: HttpClient) {}
  login(user): Promise<any> {
    //let url: string = `${this.BASE_URL}/login`;
    return this.http.post(this.url, user, this.httpOptions.toPromise();
  }

  //constructor() { }
}*/
