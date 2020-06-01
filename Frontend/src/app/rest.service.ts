import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Activities} from './learningActivity';


@Injectable({
  providedIn: 'root'
})
export class RestService {
  constructor(private http: HttpClient) { }
  projectUrl = 'http://127.0.0.1:5000/projectlist';

  readProject() {
    return this.http.get<Activities>(this.projectUrl);
  }



}
