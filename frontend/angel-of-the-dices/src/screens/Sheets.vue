<script setup>

import Sheets from "../components/charSheets.vue"

</script>

<template>
    <div class="w-4/6 h-fit flex flex-col text-center bg-bgPrimary my-20 rounded-lg p-4">
        <h1 class=" text-primary font-bold text-xl"> Fichas de Personagem </h1>
        <Sheets />
        <a href="http://localhost:5173/sheets/new" class=" mx-auto w-52 border-2 border-bgSecondary bg-secondary rounded-sm my-10">Criar uma Ficha</a>
    </div>
</template>

<style>

</style>