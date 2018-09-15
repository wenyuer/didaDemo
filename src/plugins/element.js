import Vue from 'vue'
import VueDragResize from 'vue-drag-resize'
import { Loading } from 'element-ui'
import { Row, Col, Card } from 'element-ui'
import { Input, Button, Select, Option } from 'element-ui'
import { Steps, Step } from 'element-ui'

Vue.use(Loading)
Vue.use(Row)
Vue.use(Col)
Vue.use(Card)
Vue.use(Input)
Vue.use(Button)
Vue.use(Select)
Vue.use(Option)
Vue.use(Steps)
Vue.use(Step)
Vue.use(Loading.directive)
Vue.component('vue-drag-resize', VueDragResize)

Vue.prototype.$loading = Loading.service
