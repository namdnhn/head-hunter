
<template>
    <div class="flex flex-col justify-center items-center">
            <div class="relative flex flex-col items-center rounded-[20px] w-[800px] h-[450px] mx-auto p-4 bg-white bg-clip-border shadow-3xl shadow-shadow-500 dark:!bg-navy-800 dark:text-white dark:!shadow-none">
                <div class="relative flex h-40 w-full justify-center rounded-xl bg-cover" >
                    <img src="" class="absolute flex h-60 w-full justify-center rounded-xl bg-cover"> 
                    <div class="absolute -bottom-32 flex h-[120px] w-[120px] items-center justify-center rounded-full border-[4px] border-white bg-pink-400 dark:!border-navy-700">
                        <img class="h-full w-full rounded-full" src={{company.image}} alt="" />
                    </div>
                </div> 
                <div class="mt-32 flex flex-col items-center" >
                    <h4 class="text-xl font-bold text-navy-700 dark:text-black">
                        {{ company.name }}
                    </h4>
                    <p class="text-base font-normal text-gray-600"> {{company.description}}</p>
                </div> 
                <div class="mt-6 mb-3 flex gap-14 md:!gap-14">
                    <div class="flex flex-col items-center justify-center">
                    <p class="text-2xl font-bold text-navy-700 dark:text-black">{{  company.numberJobPost }}</p>
                    <p class="text-sm font-normal text-gray-600">Job Posts</p>
                    </div>
                    <div class="flex flex-col items-center justify-center">
                    <p class="text-2xl font-bold text-navy-700 dark:text-black">
                        {{ company.numberFollowers }}
                    </p>
                    <p class="text-sm font-normal text-gray-600">Followers</p>
                    </div>
                    <div class="flex flex-col items-center justify-center">
                    <p class="text-2xl font-bold text-navy-700 dark:text-black">
                        {{ company.numberFollowing }}
                    </p>
                    <p class="text-sm font-normal text-gray-600">Following</p>
                    </div>
                </div>
            </div>  
        </div>
</template>

<script lang="ts">
    // import companys from '../.././pages/data/company.ts'

    export default {
        props:['company'],
        component:{
            name:"card-company",
        },
        data() {
            
        }
    }
</script>