import { Component, OnInit } from '@angular/core';
import { RestService } from 'src/app/rest.service';
import {Activities} from 'src/app/learningActivity';
import { User } from '../_models/user';

@Component({
  selector: 'app-project-list',
  templateUrl: './project-list.component.html',
  styleUrls: ['./project-list.component.css']
})
export class ProjectListComponent implements OnInit {
  currentUser: User;
  projects: Activities[];

  constructor(private rs: RestService) {
    this.currentUser = JSON.parse(localStorage.getItem('currentUser'));
    console.log(JSON.parse(localStorage.getItem('currentUser')));
  }
  headers = ['activity_id', 'title', 'description'];
  headersFormat = ['Activity ID', 'Title', 'Description'];

  ngOnInit() {
    this.rs.readProject().subscribe(data => {
        // @ts-ignore
        this.projects = data;
      },
      console.error
    );
  }

}
