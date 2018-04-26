import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';
import { Observable } from "rxjs/Observable";

// C:\Users\Arthur\Desktop\djangular\backend\src\static\ang
// const endpoint = '/static/ang/assets/json/videos.json'
const endpoint = "/api/videos/"

@Injectable()
export class VideoService {
  constructor(private http: Http) { }

  // **** below functions define url behavior...basic list then slug then filter

  list(){
      return this.http.get(endpoint)
              .map(response=>response.json())
              .catch(this.handleError)
  }
  featured(){
    return this.http.get(endpoint+"featured/")
            .map(response=>response.json())
            .catch(this.handleError)
}
  get(slug){
      return this.http.get(endpoint + slug + "/")
              .map(response=>response.json())
              .catch(this.handleError)
  }

  search(query){
    let queryString = `?q=${query}`
    return this.http.get(endpoint + queryString)
          .map(response=>response.json())
          .catch(this.handleError)

  }

  // Creates error and then hits redirect in the video-detail
  // private handleError (error: any, caught: any): any {
  //   if (error.status == 404) {
  //     alert("Search did not return any results!")}
  //   else {
  //     alert("Something went wrong.Please try again.")
  //   }    }

  private handleError (error: Response | any) {
    let errMsg: string;
    if (error instanceof Response) {
      const body = error.json() || "";
      const err = body.error || JSON.stringify(body);
      errMsg = `${error.status} - ${error.statusText || "" }`;
    } else { errMsg = "Server error occured.  Please try again!"; }
    console.error(errMsg);
    return Observable.throw(errMsg);
  }



}
