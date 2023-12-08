<template>
	<router-link :to="getRouterLink"
		class="w-full bg-slate-100 hover:bg-sky-100 hover:cursor-pointer p-2 rounded-lg flex justify-between items-center"
	>
		<div class="flex gap-2 items-center">
			<img
				src="https://scontent.fhan2-4.fna.fbcdn.net/v/t1.6435-1/36412437_273721143203802_2074360962202206208_n.jpg?stp=dst-jpg_p100x100&_nc_cat=105&ccb=1-7&_nc_sid=2b6aad&_nc_eui2=AeHOS_Lm8ewvSUA9lIVcAhHLrMgDE4oycXWsyAMTijJxdawX51mnh42l1bBCp7I2xJAwVfGZuGyJ629p0KsVhof5&_nc_ohc=KiZOVlAFR3YAX-k_Tvz&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.fhan2-4.fna&oh=00_AfAeuq_ZDgOVRFV_ojGB87tZarSGNykVRZX52iJbG2AddQ&oe=65819BFF"
				alt="avt"
				class="h-14 w-14 rounded-full"
			/>
			<div>
				<h2
					class="lg:text-base md:text-sm text-xs font-bold text-sky-900"
				>
					{{ fullname }}
				</h2>
				<p class="lg:text-sm text-xs text-slate-500">
					Đã gửi một nhãn dán
				</p>
			</div>
		</div>
		<p class="lg:text-sm text-xs text-slate-500">25 phút</p>
	</router-link>
</template>

<script lang="ts">
export default {
	props: ['fullname', 'user_id'],
	computed: {
		getRouterLink(): string {
			return `/chat/${this.user_id}`;
		},
	},
}
</script>

