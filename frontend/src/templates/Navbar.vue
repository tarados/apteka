<template>
    <div>
        <b-navbar toggleable="lg" type="light" variant="light">
            <b-navbar-brand href="#">
                <img src="../assets/logo.png" alt="brand">
            </b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"/>
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav class="mx-auto">
                    <b-nav-form>
                        <b-input-group size="sm">
                            <b-form-input v-model="texts" placeholder="Search"/>
                        </b-input-group>
                    </b-nav-form>

                    <b-nav-item-dropdown text="Категории" right>
                        <b-dropdown-item href="#" v-for="item in items" v-bind:key="item.category">{{ item.category }}
                        </b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>

<script>
    export default {
        name: "Navbar",
        data() {
            return {
                texts: '',
                baseClass: 'v-icon',
                items: [
                    {category: 'Акции'},
                    {category: 'Лекарственные препараты'},
                    {category: 'Красота и уход'},
                    {category: 'Товары для детей и мам'},
                    {category: 'Лечебно-косметические средства'},
                    {category: 'Медтехника и изделия медицинского назначения'},
                    {category: 'Витамины и БАДы'}
                ]
            }
        },
        methods: {
            getParam(texts) {
                this.$router.push({path: '/product/' + encodeURI(texts), params: encodeURI(texts)});
            },
            getParamOut() {
                this.$router.push({path: '/', params: 'empty'});
            }
        },
        computed: {},
        watch: {
            texts: function (seach) {
                if (this.timerId) {
                    clearTimeout(this.timerId);
                }
                this.timerId = setTimeout(() => {
                    if (seach === '')
                        this.getParamOut();
                    else
                        this.getParam(seach);
                    this.timerId = 0;
                }, 1000);
            }
        }
    }
</script>

<style scoped>

</style>