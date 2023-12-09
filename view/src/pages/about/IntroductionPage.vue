<template>
    <section class="intro bg-blue-100 py-12 xl:pt-12 xl:pb-0 overflow-hidden">
        <div class=" mt-12 container mx-auto h-full " style="color: #0c4a6e;">
            <div class="flex flex-col xl:flex-row items-center justify-between h-fit">
                <div class="intro-text xl:w-[48%] text-center xl:text-left">
                    <div class="flex items-center bg-white py-[10px] px-[20px] w-max gap-x-2 mb-26[px] rounded-full mx-auto xl:mx-0 text-xl">Head Hunter</div>
                    <div class="h1 mb-6 mt-1">Your Gateway to Talent Excellence!</div>
                    <p class="mb-[42px] md:max-w-xl">At Head Hunter, we're redefining the way talent meets opportunity. Whether you're on a quest for your dream job or seeking the perfect addition to your team, our platform is the nexus of ambition and expertise.</p>
                    <router-link :to="contactLink"><button class="flex items-center bg-white py-[10px] px-[25px] w-max gap-x-2 mb-26[px] rounded-full mx-auto xl:mx-0 text-xl">Liên hệ chúng tôi</button></router-link>
                    
                </div>
                
                
                <div class="object-contain hidden xl:flex xl:max-w-7xl w-{800} h-{600}">
                    <img src="../../assets/intro-new.png" alt="">
                </div>
            </div>
        </div>
    </section>
    <br>
    <br>
    <section class="stats section">
        <div class="container mx-auto">
            <div class="flex flex-col xl:flex-row gap-y-6 justify-between">
                <div class="stats-item flex flex-1 border-r flex-col items-center">
                    <div class="text-3xl xl:text-[64px] font-semibold text-blue-500 xl:mb-2">+5000</div>
                    <div>Candidates Joined</div>
                </div>
                <div class="stats-item flex flex-1 border-r flex-col items-center">
                    <div class="text-3xl xl:text-[64px] font-semibold text-blue-500 xl:mb-2">+50</div>
                    <div>Companies</div>
                </div>
                <div class="stats-item flex flex-1 border-r flex-col items-center">
                    <div class="text-3xl xl:text-[64px] font-semibold text-blue-500 xl:mb-2">5</div>
                    <div>Total Branches</div>
                </div>
                <div class="stats-item flex flex-1 flex-col items-center">
                    <div class="text-3xl xl:text-[64px] font-semibold text-blue-500 xl:mb-2">1</div>
                    <div>Year</div>
                </div>
            </div>
        </div>
    </section>
    <br>
    <br>
    <section class="services">
        <div class="bg-blue-200 bg-cover bg-no-repeat max-w-[1466px] mx-4 xl:mx-auto rounded-[20px] xl:pt-[70px] px-6 xl:px-0 relative h-[368px] flex items-center xl:items-start -z-10">
            <div class="container mx-auto flex flex-col">
                <div class=" flex items-center flex-col xl:flex-row xl:mb-[60px]">
                    <h2 class="text-5xl ml-0 text-while flex-1 mb-4 xl:mb-0 text-center xl:text-center items-center md:text-3xl sm:text-xl min-w-sm">Our best services for your career future</h2>
                    <p class="text-white text-xl flex-1 text-center xl:text-left max-w-4xl xl:max-w-none md:text-xl sm:text-base">Dive into a world where success is not just a goal; it's a journey we embark upon together. Join Head Hunter today and witness the power of connections, the synergy of talent, and the realization of professional dreams.</p>
                </div>
                
            </div>
            
        </div>
        
    </section>
    <section class="team section">
        <div class="container mx-auto text-center">
            <h2 class="h2 mb-[50px] text-center content-center xl:text-left">Đội ngũ điều hành</h2>
        </div>


    </section>
    <section>
        <section class="px-12">
    <div class="max-w-3xl xs:w-lg md:w-xl mx-auto relative">

        <input id="article-01" type="radio" name="slider" class="sr-only peer/01">
        <input id="article-02" type="radio" name="slider" class="sr-only peer/02">
        <input id="article-03" type="radio" name="slider" class="sr-only peer/03" checked>
        <input id="article-04" type="radio" name="slider" class="sr-only peer/04">
        <input id="article-05" type="radio" name="slider" class="sr-only peer/05">

        <div class="
            absolute inset-0 scale-[67.5%] z-20 transition-all duration-500 ease-[cubic-bezier(0.25,1,0.5,1)]
            peer-focus-visible/01:[&_article]:ring
            peer-focus-visible/01:[&_article]:ring-indigo-300
            peer-checked/01:relative
            peer-checked/01:z-50
            peer-checked/01:translate-x-0
            peer-checked/01:scale-100
            peer-checked/01:[&>label]:pointer-events-none
            peer-checked/02:-translate-x-20
            peer-checked/02:scale-[83.75%]
            peer-checked/02:z-40
            peer-checked/03:-translate-x-40
            peer-checked/03:z-30
            peer-checked/04:-translate-x-40                    
            peer-checked/04:opacity-0
            peer-checked/05:-translate-x-40
        ">
            <label class="absolute inset-0" for="article-01"><span class="sr-only"></span></label>
            <article class="bg-white p-6 rounded-lg shadow-2xl">
                <header class="mb-2">
                    <h1 class="text-xl font-bold text-slate-900">Đỗ Nhữ Hoàng Nam</h1>
                </header>
                <img src="../../assets/thien.jpg" alt="">
                <footer class="text-right">
                    <a class="text-sm font-medium text-indigo-500 " >Chủ tịch Head Hunter</a>
                </footer>
            </article>
        </div>

        <div class="
            absolute inset-0 scale-[67.5%] z-20 transition-all duration-500 ease-[cubic-bezier(0.25,1,0.5,1)]
            peer-focus-visible/02:[&_article]:ring
            peer-focus-visible/02:[&_article]:ring-indigo-300                        
            peer-checked/01:translate-x-20
            peer-checked/01:scale-[83.75%]
            peer-checked/01:z-40
            peer-checked/02:relative
            peer-checked/02:z-50
            peer-checked/02:translate-x-0
            peer-checked/02:scale-100
            peer-checked/02:[&>label]:pointer-events-none
            peer-checked/03:-translate-x-20
            peer-checked/03:scale-[83.75%]
            peer-checked/03:z-40
            peer-checked/04:-translate-x-40
            peer-checked/04:z-30
            peer-checked/05:-translate-x-40 
            peer-checked/05:opacity-0
        ">
            <label class="absolute inset-0" for="article-02"><span class="sr-only">Focus on the big picture</span></label>
            <article class="bg-white p-6 rounded-lg shadow-2xl">
                <header class="mb-2">
                    
                    <h1 class="text-xl font-bold text-slate-900">Tô Lâm Sơn</h1>
                </header>
                <img src="../../assets/thien.jpg" alt="">
                <footer class="text-right">
                    <a class="text-sm font-medium text-indigo-500 " >Giám đốc bộ phận kỹ thuật Head Hunter</a>
                </footer>
            </article>
        </div>

        <div class="
            absolute inset-0 scale-[67.5%] z-20 transition-all duration-500 ease-[cubic-bezier(0.25,1,0.5,1)]
            peer-focus-visible/03:[&_article]:ring
            peer-focus-visible/03:[&_article]:ring-indigo-300                          
            peer-checked/01:translate-x-40
            peer-checked/01:z-30
            peer-checked/02:translate-x-20
            peer-checked/02:scale-[83.75%]
            peer-checked/02:z-40
            peer-checked/03:relative
            peer-checked/03:z-50
            peer-checked/03:translate-x-0
            peer-checked/03:scale-100
            peer-checked/03:[&>label]:pointer-events-none
            peer-checked/04:-translate-x-20
            peer-checked/04:scale-[83.75%]
            peer-checked/04:z-40
            peer-checked/05:-translate-x-40
            peer-checked/05:z-30                  
        ">
            <label class="absolute inset-0" for="article-03"><span class="sr-only">Focus on the big picture</span></label>
            <article class="bg-white p-6 rounded-lg shadow-2xl">
                <header class="mb-2">
                    <h1 class="text-xl font-bold text-slate-900">Nguyễn Đức Thiện</h1>
                </header>
                <img src="../../assets/thien.jpg" alt="">
                <footer class="text-right">
                    <a class="text-sm font-medium text-indigo-500 hover:underline" href="#0">Giám đốc điều hành Head Hunter </a>
                </footer>
            </article>
        </div>

        <div class="
            absolute inset-0 scale-[67.5%] z-20 transition-all duration-500 ease-[cubic-bezier(0.25,1,0.5,1)]
            peer-focus-visible/04:[&_article]:ring
            peer-focus-visible/04:[&_article]:ring-indigo-300                          

            peer-checked/01:translate-x-40 
            peer-checked/01:opacity-0
            
            peer-checked/02:translate-x-40
            peer-checked/02:z-30
            
            peer-checked/03:translate-x-20
            peer-checked/03:scale-[83.75%]
            peer-checked/03:z-40

            peer-checked/04:relative
            peer-checked/04:z-50
            peer-checked/04:translate-x-0
            peer-checked/04:scale-100
            peer-checked/04:[&>label]:pointer-events-none
            
            peer-checked/05:-translate-x-20
            peer-checked/05:scale-[83.75%]
            peer-checked/05:z-40
        ">
            <label class="absolute inset-0" for="article-04"><span class="sr-only">Focus on the big picture</span></label>
            <article class="bg-white p-6 rounded-lg shadow-2xl">
                <header class="mb-2">
                    <h1 class="text-xl font-bold text-slate-900">Nguyễn Thị Thanh Thủy</h1>
                </header>
                <img src="../../assets/thien.jpg" alt="">
                <footer class="text-right">
                    <a class="text-sm font-medium text-indigo-500 ">Giám đốc bộ phận phát triển và sáng tạo Head Hunter</a>
                </footer>
            </article>
        </div>  

        <div class="
            absolute inset-0 scale-[67.5%] z-20 transition-all duration-500 ease-[cubic-bezier(0.25,1,0.5,1)]
            peer-focus-visible/05:[&_article]:ring
            peer-focus-visible/05:[&_article]:ring-indigo-300                          
            peer-checked/01:translate-x-40 
            peer-checked/02:translate-x-40 
            peer-checked/02:opacity-0
            peer-checked/03:translate-x-40
            peer-checked/03:z-30
            peer-checked/04:translate-x-20
            peer-checked/04:scale-[83.75%]
            peer-checked/04:z-40
            peer-checked/05:relative
            peer-checked/05:z-50
            peer-checked/05:translate-x-0
            peer-checked/05:scale-100
            peer-checked/05:[&>label]:pointer-events-none
        ">
            <label class="absolute inset-0" for="article-05"><span class="sr-only">Focus on the big picture</span></label>
            <article class="bg-white p-6 rounded-lg shadow-2xl">
                <header class="mb-2">
                    <h1 class="text-xl font-bold text-slate-900">Cao Thị Phương Anh</h1>
                </header>
                <img src="../../assets/thien.jpg" alt="">
                <footer class="text-right">
                    <a class="text-sm font-medium text-indigo-500 " >Giám đốc tài chính Head Hunter</a>
                </footer>
            </article>
        </div>                  
    </div>
</section>
    </section>
    <br><br><br>
</template>

<script lang="ts">
    export default {
        computed:{
            contactLink(){
                return "/contactpage"
            }
        }
    }
</script>