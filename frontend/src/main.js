import Vue from 'vue'
import App from './App.vue'
import router from "./router";
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import feather from 'vue-icon'


Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(feather, 'v-icon');

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
