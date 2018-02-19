import axios from 'axios'
import * as url from './urlConfig'

// Product
export const requestProduct = {
  List: params => { return axios.get(url.product, { params: params }).then(res => res.data) }
}

// Store
export const requestStore = {
  List: params => { return axios.get(url.store, { params: params }).then(res => res.data) }
}

// Method
export const requestMethod = {
  List: params => { return axios.get(url.method, { params: params }).then(res => res.data) }
}

// Cart
export const requestCart = {
  List: params => { return axios.get(url.cart, { params: params }).then(res => res.data) },
  Create: params => { return axios.post(url.cart, params).then(res => res.data) },
  Update: params => { return axios.patch(url.cart, params).then(res => res.data) }
}
