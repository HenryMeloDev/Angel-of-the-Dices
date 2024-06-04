<template>
    <div class=" grid grid-cols-4 gap-4 bg-darkgrayColor rounded-xl p-10">
        <div v-for="sheet in charSheets" :key="sheet.id"
        class=" border border-bgSecondary bg-lightgrayColor text-primary font-bold rounded-lg p-4"
        >
        <h3>{{ sheet.nome }}</h3>
        <h3>{{ sheet.origem }}</h3>
        <h3>{{ sheet.classe }} {{ sheet.trilha }}</h3>
        <h3>{{ sheet.nivel }}</h3>
        </div>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            charSheets:[]
        }
    },

    methods: {
        getResponse(){
            const path = 'http://localhost:5000/sheets/'

            axios.get(path)
            .then((res) => {
                console.log(res.data)
                this.charSheets = res.data.sheets;
            })
            .catch ((err) => {
                console.error(err);
            });
        }
    },
    created() {
        this.getResponse();
    },
}
</script>

<style>

</style>