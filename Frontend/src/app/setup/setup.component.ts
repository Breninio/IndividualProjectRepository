import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import {Activities} from '../learningActivity';
import { NgForm } from '@angular/forms';
import { FormBuilder} from '@angular/forms';

import { AddprojectService} from '../addproject.service';


@Component({
  selector: 'app-setup',
  templateUrl: './setup.component.html',
  styleUrls: ['./setup.component.css']
})
export class SetupComponent implements OnInit {
  setupForm = new FormGroup({
    activityTitle: new FormControl(''),
    activityDescription: new FormControl(''),
    startDate: new FormControl(''),
    endDate: new FormControl(''),
    reason: new FormControl(''),
    learnings: new FormControl(''),
    application: new FormControl(''),
    support: new FormControl(''),
    p1: new FormControl(''),
    p2: new FormControl(''),
  });

  constructor(private addprojectservice: AddprojectService) { }

  ngOnInit() {
  }
  addProject() {}
  onSubmit() {
    console.warn(this.setupForm.value);
    const activities = {} as Activities;
    activities.activity_title = this.setupForm.value.activityTitle;
    activities.activity_description = this.setupForm.value.activityDescription;
    activities.activity_startDate = this.setupForm.value.startDate;
    activities.activity_endDate = this.setupForm.value.endDate;
    activities.activity_reason = this.setupForm.value.reason;
    activities.activity_learnings = this.setupForm.value.learnings;
    activities.activity_application = this.setupForm.value.application;
    activities.activity_support = this.setupForm.value.support;
    activities.activity_participant1 = this.setupForm.value.p1;
    activities.activity_participant2 = this.setupForm.value.p2;
    activities.activity_participant3 = this.setupForm.value.p3;
    activities.activity_participant4 = this.setupForm.value.p4;
    activities.activity_participant5 = this.setupForm.value.p5;
    this.addprojectservice.addProject(activities).subscribe(data => this.setupForm);
    console.warn(activities.activity_title);
  }
}
