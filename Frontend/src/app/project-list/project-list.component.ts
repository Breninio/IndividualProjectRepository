import { Component, OnInit } from '@angular/core';
import { RestService } from 'src/app/rest.service';
import {Activities} from 'src/app/learningActivity';

@Component({
  selector: 'app-project-list',
  templateUrl: './project-list.component.html',
  styleUrls: ['./project-list.component.css']
})
export class ProjectListComponent implements OnInit {
  projects: Activities[];

  constructor(private rs: RestService) {
  }
  headers = ['activity_id', 'Title', 'description']

  ngOnInit() {
    this.rs.readProject().subscribe(data => {
        // @ts-ignore
        this.projects = data;
      },
      console.error
    );
  }}
