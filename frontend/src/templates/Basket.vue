<template>
    <div class="container">
        <div class="wrapper">
            <div id="header">
                <div class="title">
                    <i>Basket</i>
                </div>
            </div>
            <div id="contentBasket">
                <div class="col product">sdfsd</div>
                <div class="col quantity">erwew</div>
                <div class="col total">wewe</div>
                <div class="col deleteOrder">gerer</div>
            </div>
            <div id="footer">
                <b-button variant="success" @click="toHome">Button</b-button>
                <b-button variant="success" @click="toHome">Button</b-button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Basket",
        methods: {
            toHome() {
                this.$router.go(-1);
            },
            currentPage() {
                // eslint-disable-next-line no-console
                console.log(this.$router);
            }
        },
        mounted() {
            this.currentPage();
        }
    }
</script>

<style scoped>
    .container {
       border: 1px solid red;
    }

    .wrapper {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
    }

    #header {
        width: 100%;
        height: 3em;
        background-color: gold;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: center
    }

    #contentBasket {
        width: 100%;
        min-height: 20px;
        background-color: #6DDCBD;
        margin: 0 -15px;
    }

    .wrapper .col {
        text-align: center;
        border: 1px solid yellow;
        margin: 5px;
        width: calc(100% / 4 - 10px);
        display: inline-block;
    }

    #footer {

    }
</style>