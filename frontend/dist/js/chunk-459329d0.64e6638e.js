(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-459329d0"],{"02a9":function(t,s,c){"use strict";c.r(s);var i=function(){var t=this,s=t.$createElement,c=t._self._c||s;return c("div",{staticClass:"container"},[c("div",{attrs:{id:"header"}},[c("div",{staticClass:"totalPrice"},[c("i",[t._v("Всего к оплате: "),c("span",[t._v(t._s(t.totalPrice)+" руб.")])])])]),c("div",{staticClass:"wrapper"},[t._l(t.allProducts,(function(s,i){return c("div",{key:i,staticClass:"contentBasket"},[c("div",{staticClass:"photo"},[c("img",{attrs:{src:s.photo,alt:s.title}})]),c("div",{staticClass:"product"},[c("div",{staticClass:"title",domProps:{textContent:t._s(s.title)}}),c("div",{staticClass:"manufacturer",domProps:{textContent:t._s(s.manufacturer)}}),c("div",{staticClass:"price",domProps:{textContent:t._s(s.price+" руб.")}})]),c("div",{staticClass:"quantity"},[c("b-button",{attrs:{variant:"outline"},on:{click:function(s){return t.minusQuantity(i)}}},[c("custom-icon",{staticClass:"custom-icon",attrs:{name:"minus-square"}})],1),c("div",{staticClass:"productQuantity",domProps:{textContent:t._s(s.quantity)}}),c("b-button",{attrs:{variant:"outline"},on:{click:function(s){return t.plusQuantity(i)}}},[c("custom-icon",{staticClass:"custom-icon",attrs:{name:"plus-square"}})],1)],1),c("div",{staticClass:"total"},[t._v(t._s(s.valueProduct.toFixed(1))+" руб.")]),c("b-button-close",{staticClass:"deleteOrder",on:{click:function(s){return t.deleteOrder(i)}}},[c("custom-icon",{staticClass:"custom-icon",attrs:{name:"x"}})],1)],1)})),c("div",{attrs:{id:"footer"}},[c("b-button",{staticClass:"basket",attrs:{variant:"outline-primary"},on:{click:t.toHome}},[c("custom-icon",{staticClass:"custom-icon",attrs:{name:"chevron-left"}}),t._v(" Продолжить покупки ")],1),c("b-button",{staticClass:"basket",attrs:{variant:"success"},on:{click:t.toCheckout}},[t._v(" Оформить заказ ")])],1)],2)])},o=[],a=c("5530"),e=c("f1dd"),n=c("2f62"),r={name:"Basket",components:{customIcon:e["a"]},computed:Object(a["a"])({},Object(n["b"])(["allProducts"]),{},Object(n["b"])(["getTotalPrice"]),{},Object(n["c"])(["basketProducts"]),{totalPrice:function(){return 0===this.allProducts.length?0:this.getTotalPrice}}),methods:{toHome:function(){this.$router.go(-1)},toCheckout:function(){this.$router.push("/basket/checkout"),this.$store.commit("addTotalPriceToCheck")},deleteOrder:function(t){this.$store.commit("delProduct",t)},minusQuantity:function(t){this.$store.commit("decrement",t)},plusQuantity:function(t){this.$store.commit("increment",t)}}},u=r,l=(c("c068"),c("2877")),d=Object(l["a"])(u,i,o,!1,null,"bb14f58e",null);s["default"]=d.exports},"9c28":function(t,s,c){},c068:function(t,s,c){"use strict";var i=c("9c28"),o=c.n(i);o.a}}]);
//# sourceMappingURL=chunk-459329d0.64e6638e.js.map