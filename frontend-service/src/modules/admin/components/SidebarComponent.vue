<script setup lang="ts">
import { ref } from 'vue';

const props = defineProps<{
	icons: Array<{
		name: string;
		component: any;
		path: string;
	}>;
}>();

const tooltipArrState = ref(Array(props.icons.length).fill(false));
</script>

<template>
  <div
    v-once
    class="sidebar-sub-container"
  >
    <template
      v-for="(icon, index) in icons"
      :key="icon.name"
    >
      <RouterLink
        :to="icon.path"
        active-class="active"
        class="icon-container"
        @mouseenter="tooltipArrState[index] = true"
        @mouseleave="tooltipArrState[index] = false"
      >
        <!-- Icon -->
        <component :is="icon.component" />

        <!-- Tooltip -->
        <template v-if="tooltipArrState[index]">
          <div class="tooltip-container">
            <p>{{ icon.name }}</p>
          </div>
        </template>
      </RouterLink>
    </template>
  </div>
</template>

<style scoped>
.sidebar-sub-container {
	height: 100%;
	width: 100%;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: flex-start;
	background-color: #ffffff;
	border-radius: 20px;
	box-shadow: 0px 10px 15px -3px rgba(0, 0, 0, 0.1);
	position: sticky;
}
.icon-container {
	margin: 10px 0;
	width: 65%;
	height: 6%;
	background-color: transparent;
	display: flex;
	flex-direction: row;
	justify-content: center;
	align-items: center;
	border-radius: 10px;
	border-color: transparent;
	cursor: pointer;
	position: relative;
	color: black;
}
.icon-container:hover {
	background-color: #598bff;
	color: white;
}

.active {
	background-color: #598bff;
	color: white;
}

.tooltip-container {
	position: absolute;
	z-index: 2;
	left: 50px;
	background-color: #1c2536;
	color: white;
	padding: 4px 8px;
	border-radius: 8px;
}

.tooltip-container p {
	font-size: 12px;
	font-weight: 600;
}

/* .icon-container:last-child {
	margin-top: auto;
} */
</style>
