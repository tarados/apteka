<template>
    <div class="placeFarmacy container">
        <button class="btn btn-success" @click="$emit('onProduct')">Product</button>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                modes: ['multi', 'single', 'range'],
                fields: ['selected', 'isActive', 'age', 'first_name', 'last_name'],
                items: [
                    {isActive: true, age: 40, first_name: 'Dickerson', last_name: 'Macdonald'},
                    {isActive: false, age: 21, first_name: 'Larsen', last_name: 'Shaw'},
                    {isActive: false, age: 89, first_name: 'Geneva', last_name: 'Wilson'},
                    {isActive: true, age: 38, first_name: 'Jami', last_name: 'Carney'}
                ],
                selectMode: 'multi',
                selected: []
            }
        },
        methods: {
            rowSelected(items) {
                this.selected = items
            }
        }
    }
</script>

<style scoped>

</style>