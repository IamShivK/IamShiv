import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { JwtHelperService } from '@auth0/angular-jwt'

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  static herlper : JwtHelperService = new JwtHelperService(); 
  baseurl : string ="http//localhost:5000"
  constructor(private http : HttpClient) { }

  logins(user:any,callback:any){
    this.http.post(this.baseurl+"/login",user).subscribe((Response:any)=>{
      console.log(Response.access_token)
      localStorage.setItem('access_token', Response.access_token)
      callback(true)
    },
  (error)=>{
    callback(false)
  })
  }
 isLoggedIn(){
   let token = localStorage.getItem('access_token');
   if(!token)
    return false;
   let val = AuthService.herlper.isTokenExpired(token) 
   
   if(!val){
     return true
   }else{
     return false
   }
 }

  logout(){
    localStorage.removeItem('access_token')
  }
}
