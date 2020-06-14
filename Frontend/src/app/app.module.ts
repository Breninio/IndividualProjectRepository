import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import {RestService} from './rest.service';
import { SetupComponent } from './setup/setup.component';
import { ProjectListComponent } from './project-list/project-list.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpErrorHandler } from './http-error-handler.service';
import { MessageService } from './message.service';
import { FormsModule} from '@angular/forms';
import {AddprojectService} from './addproject.service';
import { LoginComponent } from './login/login.component';
import {AuthService} from './auth.service';
import { RegisterComponent } from './register/register.component';
import {AuthenticationService} from './_services/authentication.service';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { JwtInterceptor} from './_helpers/jwt.interceptor';
import { ErrorInterceptor } from './_helpers/error.interceptor';
import { HomeComponent } from './home/home.component';
import { AlertComponent } from './_components/alert.component';
import { PagelayoutComponent } from './pagelayout/pagelayout.component';


@NgModule({
  declarations: [
    AppComponent,
    SetupComponent,
    ProjectListComponent,
    LoginComponent,
    RegisterComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    AlertComponent,
    PagelayoutComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule
  ],
  providers: [RestService, HttpErrorHandler,
    MessageService, AddprojectService, AuthenticationService, { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true }, ],
  bootstrap: [AppComponent]
})
export class AppModule { }
