import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Activities} from './learningActivity';
import { HttpHeaders } from '@angular/common/http';
import {HttpParams} from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class RestService {
  constructor(private http: HttpClient) { }
  projectUrl = 'http://127.0.0.1:5000/projectlist';



  readProject() {
    let params = new HttpParams();
    params = params.append('username', JSON.parse(localStorage.getItem('currentUser')).username);

    return this.http.get<Activities>(this.projectUrl, {params});
    //return this.http.get<Activities>(this.projectUrl);
  }



}
