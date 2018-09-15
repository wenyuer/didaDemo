import axios from 'axios'

const service = axios.create({
  baseURL: 'http://127.0.0.1:5000/dida/'
})

export default {
  get: (url, callback) => {
    service.request({
      method: 'GET',
      url: url
    }).then(response => {
      callback(response.data)
    })
  },
  post: (url, data, callback) => {
    service.request({
      method: 'POST',
      url: url,
      data: data
    }).then(response => {
      callback(response.data)
    })
  }
}
