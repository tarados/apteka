(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-035654b4"],{"4d53":function(t,e,r){"use strict";var i=r("8390"),s=r.n(i);s.a},"5b5c":function(t,e,r){"use strict";var i=r("6198"),s=r.n(i);s.a},"5e2c":function(t,e,r){t.exports=r.p+"img/no-img.88294ef3.png"},6198:function(t,e,r){},7542:function(t,e,r){"use strict";var i=r("aeea"),s=r.n(i);s.a},8390:function(t,e,r){},"8a11":function(t,e,r){"use strict";var i=r("ae67"),s=r.n(i);s.a},ad9e:function(t,e,r){"use strict";r.r(e);var i=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"container"},[r("div",[t.query?r("h3",[t._v(' Результаты поиска по запросу "'+t._s(t.query)+'" ')]):r("h3",[t._v("Первые пять позиций прайса")])]),r("Sorting",{attrs:{count:t.count},on:{sortingProductPrice:t.sortingProductPrice,filterProduct:t.filterProduct}}),t.filter?r("Filtration",{attrs:{"filterable-list":t.products,"filterable-field":"manufacturer"},on:{filteredItem:t.filteredManufacturer}}):r("div"),r("div",{staticClass:"products"},t._l(t.productsFiltered,(function(t){return r("div",{key:t.title,staticClass:"item"},[r("Product",{attrs:{product:t}})],1)})),0)],1)},s=[],n=(r("4de4"),r("a15b"),r("ac1f"),r("466d"),r("96cf"),r("1da1")),c=r("b414"),o=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"product"},[t._m(0),r("div",{staticClass:"title",domProps:{textContent:t._s(t.product.title)}}),r("div",{staticClass:"manufacturer",domProps:{textContent:t._s(t.product.manufacturer)}}),r("div",{staticClass:"price",domProps:{textContent:t._s(t.product.price+" руб.")}}),r("b-button",{staticClass:"action",attrs:{variant:"success"},on:{click:t.toBasket}},[r("custom-icon",{staticClass:"custom-icon",attrs:{name:"shopping-cart"}}),r("span",[t._v("Купить")])],1)],1)},a=[function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"pic"},[i("img",{attrs:{id:"myImg",src:r("5e2c"),alt:""}})])}],u=(r("b680"),r("f1dd")),l=r("60c4"),d={name:"Product",components:{customIcon:u["a"]},props:{product:{type:Object}},methods:{toBasket:function(){this.$router.push("/basket"),this.product.photo=document.getElementById("myImg").src,this.product.quantity=1,this.product.valueProduct=parseFloat((this.product.quantity*this.product.price).toFixed(1)),l["a"](this.product),this.$store.commit("addProduct",this.product)}}},f=d,p=(r("5b5c"),r("2877")),m=Object(p["a"])(f,o,a,!1,null,"16e5fa1e",null),h=m.exports,v=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"sort-list"},[r("div",{staticClass:"counter"},[r("span",[t._v("Товаров: "+t._s(t.count))])]),r("div",{staticClass:"sorting"},[r("b-dropdown",{staticClass:"m-2",attrs:{split:"","split-variant":"outline-info",variant:"info",text:t.text}},[r("b-dropdown-item",{on:{click:t.sortingFromMin}},[t._v("От дешевых")]),r("b-dropdown-item",{on:{click:t.sortingFromMax}},[t._v("От дорогих")])],1),r("button",{staticClass:"btn btn-danger",attrs:{type:"button"},on:{click:t.filterProduct}},[t.state?r("i",[r("custom-icon",{staticClass:"custom-icon",attrs:{name:"filter"}})],1):r("i",[r("custom-icon",{staticClass:"custom-icon",attrs:{name:"activity"}})],1),r("span",[t._v("Фильтр")])])],1)])},b=[],g=(r("a9e3"),{name:"Sorting",components:{customIcon:u["a"]},props:{count:Number},data:function(){return{text:"Сортировка",state:!0}},methods:{sortingFromMin:function(){this.text="От дешевых",this.$emit("sortingProductPrice","min")},sortingFromMax:function(){this.text="От дорогих",this.$emit("sortingProductPrice","max")},filterProduct:function(){this.$emit("filterProduct",this.state),this.state=!this.state}}}),x=g,P=(r("4d53"),Object(p["a"])(x,v,b,!1,null,"7cca6f5e",null)),y=P.exports,_=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",{staticClass:"filtered"},[r("b-form-group",{staticClass:"inline-group"},[r("b-form-checkbox-group",{attrs:{options:t.options,name:"flavour-1a"},model:{value:t.selected,callback:function(e){t.selected=e},expression:"selected"}})],1),r("b-form-group",{staticClass:"stacked"},[r("b-form-checkbox-group",{attrs:{options:t.options,name:"flavour-2a",stacked:""},model:{value:t.selected,callback:function(e){t.selected=e},expression:"selected"}})],1)],1)},C=[],k=(r("99af"),r("4160"),r("159b"),r("a30f")),F=r.n(k),$={name:"Filters",props:{filterableList:{type:Array},filterableField:{type:String}},data:function(){return{selected:[],options:[]}},methods:{createOptionsList:function(){var t=this;this.filterableList.forEach((function(e){e.text=e[t.filterableField]}));var e=F()(this.filterableList,"text"),r=[];for(var i in e)r.push(i);this.options=this.options.concat(r)},selectedItem:function(){this.$emit("filteredItem",this.selected)}},mounted:function(){this.createOptionsList()},watch:{selected:function(){this.selectedItem()}}},w=$,q=(r("8a11"),Object(p["a"])(w,_,C,!1,null,"3259d20a",null)),I=q.exports,L={components:{Product:h,Filtration:I,Sorting:y},data:function(){return{query:"",filter:null,manufacturerFilter:null,products:[],count:0}},computed:{productsFiltered:function(){if(this.manufacturerFilter&&this.manufacturerFilter.length){var t=this.manufacturerFilter.join("|"),e=this.products.filter((function(e){return e.text.match(t)}));return this.count=e.length,e}return this.count=this.products.length,this.products}},methods:{loadProducts:function(t){var e=this;return Object(n["a"])(regeneratorRuntime.mark((function r(){var i;return regeneratorRuntime.wrap((function(r){while(1)switch(r.prev=r.next){case 0:return t&&t.length||(t=""),r.next=3,c["a"]("products",{query:t});case 3:i=r.sent,e.products=i.products,e.count=e.products.length;case 6:case"end":return r.stop()}}),r)})))()},checkQueryAndLoadProducts:function(){this.$route.params.textseach!==this.query&&(this.query=this.$route.params.textseach,this.loadProducts(this.query))},sortingProductPrice:function(t){var e=function(e,r){return"min"===t?e.price>r.price?1:-1:"max"===t?e.price<r.price?1:-1:void 0};this.products.sort(e)},filterProduct:function(t){!0===t?this.filter=t:(this.filter=null,this.manufacturerFilter=null)},filteredManufacturer:function(t){this.manufacturerFilter=t}},mounted:function(){this.checkQueryAndLoadProducts()},updated:function(){""!==this.query&&void 0!==this.query||(this.$route.params.textseach="")},watch:{$route:function(){this.checkQueryAndLoadProducts()}}},O=L,j=(r("7542"),Object(p["a"])(O,i,s,!1,null,"6b177ff4",null));e["default"]=j.exports},ae67:function(t,e,r){},aeea:function(t,e,r){}}]);
//# sourceMappingURL=chunk-035654b4.5c90ed8b.js.map