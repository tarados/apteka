<template>
    <div class="productStorage">
        <app-poduct v-if="state == 'product'"></app-poduct>
        <app-farmacy v-else-if="state == 'farmacy'"
                     @onProduct="onProduct"
        >
        </app-farmacy>
        <app-maps v-else-if="state == 'maps'"></app-maps>
        <div v-else>Unknown state</div>
    </div>

</template>

<script>
    export default {
        data() {
            return {
                state: 'maps'
            }
        },
        methods: {
            onProduct(){
                this.state = 'product'
            }
        }
    }
</script>

<style scoped>

</style>
