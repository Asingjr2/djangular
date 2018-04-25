import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

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

    // return this.http.get(endpoint)
    //           .map(response=>{
    //                  let data = []
    //                  let req = response.json().filter(item=>{
    //                                 if (item.name.indexOf(query) >=0) {
    //                                      data.push(item)
    //                                 }
    //                             })

    //                  return data
    //            })
    //           .catch(this.handleError)

  }

  private handleError(error:any, caught:any): any{
      console.log(error, caught)
  }

}
