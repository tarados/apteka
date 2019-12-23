<template>
    <div class="sort-list">
        <div class="counter">
            <span>Товаров: {{ count }}</span>
        </div>
        <div class="sorting">
            <b-dropdown
                    split
                    split-variant="outline-info"
                    variant="info"
                    text="По релевантности"
                    class="m-2 dr"
            >
                <b-dropdown-item href="#">От дешевых</b-dropdown-item>
                <b-dropdown-item href="#">От дорогих</b-dropdown-item>
            </b-dropdown>
            <button type="button" class="btn btn-danger">
                <custom-icon name="filter" class="custom-icon"/>
                <span>Фильтр</span>
            </button>
        </div>
    </div>
</template>

<script>
    import customIcon from 'vue-icon/lib/vue-feather.esm'

    export default {
        name: "Sorting",
        components: {
            // eslint-disable-next-line vue/no-unused-components
            customIcon
        },
        props: {
            product: {
                type: Object
            },
            count: Number
        }
    }
</script>

<style scoped>
    .sort-list {
        display: flex;
        flex-wrap: nowrap;
        justify-content: space-between;
        align-items: center;
        margin: 0 5px;
    }

    .counter {
        float: left;
    }

    .sorting {

    }

    .custom-icon {
        width: 24px;
    }

    .counter span {
        margin-left: 5px;
        color: #4d4d4d;
        font-size: 16px;
    }

</style>