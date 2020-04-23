<template>
    <div class="orderSuccessful">
        <p>Ваша заявка принята! Спасибо за покупку!</p>
        <b-button variant="outline-primary" @click="backToMain">Вернуться на главную страницу</b-button>
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
    }

    p {
        font-size: 25px;
        font-weight: 600;
        font-style: italic;
    }
</style>