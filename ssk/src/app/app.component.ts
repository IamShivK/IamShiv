import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';
import { AuthService } from './auth.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  loginError : boolean=false;
  
  onBlur(fn:any){
    console.log(fn);
  }
  
  onSubmit(user:any){
    this.log.logins(user,(loginflag : any)=>{
      if(loginflag){
        this.route.navigateByUrl("/home")
      }else{
        this.loginError=true;
      }
    })

  }
 constructor(private log : AuthService, private route : Router) {}
}
