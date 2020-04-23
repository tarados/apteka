<template>
    <div class="container">
        <div class="orderSuccessful">
            <p>Ваша заявка принята! Спасибо за покупку!</p>
            <b-button variant="outline-primary" @click="backToMain">Вернуться на главную страницу</b-button>
        </div>
    </div>

</template>

<script>
    export default {
        name: "Successful",
        methods: {
            backToMain() {
                this.$router.go(-3);
            }
        }
    }
</script>

<style scoped>
    .orderSuccessful {
        text-align: center;
        margin: 20px 0;
        padding: 15px;
        border: 1px solid green;
        background-color: #f2f2f2;
        border-radius: 3px;
    }

    p {
        font-size: 25px;
        font-weight: 600;
        font-style: italic;
    }
</style>