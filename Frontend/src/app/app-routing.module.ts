import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {SetupComponent} from './setup/setup.component';
import {ProjectListComponent} from './project-list/project-list.component';
import {LoginComponent} from './login/login.component';
import {RegisterComponent} from './register/register.component';
import { HomeComponent} from './home/home.component';
import {AuthGuard} from './_helpers/auth.guard';
import {PagelayoutComponent} from './pagelayout/pagelayout.component';


const routes: Routes = [
  {path: '', component: LoginComponent},
  {path: 'login', component: LoginComponent},
  {path: 'register', component: RegisterComponent},
  {path: 'projectlist', component: ProjectListComponent},
  {path: 'setup', component: SetupComponent},

  // otherwise redirect to home
  {path: '**', redirectTo: ''}
 /* {
    path: '', component: LoginComponent,
    children: [
      {path: 'register', component: RegisterComponent}
    ]
  },
  {
    path: 'route2', component: PagelayoutComponent,
    children: [

    ]
  }*/
  ];

//@NgModule({
  //imports: [RouterModule.forRoot(routes)],
  //exports: [RouterModule]
//})
//export class AppRoutingModule { }

export const appRoutingModule = RouterModule.forRoot(routes);
