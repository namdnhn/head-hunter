<template>
    <li class="flex gap-4 items-center">
        <font-awesome-icon icon="fa-solid fa-file" class="bg-slate-200 text-xl text-green-600 p-4 rounded-lg" />
        <span>
            <h2 class=" text-sky-900 font-semibold text-xs md:text-sm lg:text-base hover:cursor-pointer">{{ fileName }}
            </h2>
            <p class="text-gray-500 text-xs md:text-sm">{{ time }}</p>
        </span>
    </li>
</template>

<script lang="ts">
    export default {
        props: {
            fileName: {
                type: String,
                required: true,
            },
            time: {
                type: String,
                required: true,
            },
        }
    }
</script>