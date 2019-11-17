import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import '../src/css/mystyle.css'

import AppStartscreen from "./components/Home";
import AppProduct from "./components/Product.vue";
import AppFarmacy from "./components/Farmacy.vue";
import AppMaps from "./components/Maps.vue";

Vue.component("AppStartscreen", AppStartscreen);
Vue.component("AppPoduct", AppProduct);
Vue.component("AppFarmacy", AppFarmacy);
Vue.component("AppMaps", AppMaps);
Vue.config.productionTip = false;
Vue.use(BootstrapVue);

new Vue({
  render: h => h(App),
}).$mount('#app');
