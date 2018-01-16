<template>
  <vue-clip :options="options" :on-added-file="fileAdded" class="uploader">
    <template slot="clip-uploader-action" slot-scope="props">
      <div class="uploader-action" v-bind:class="{dragging: props.dragging}">
        <div class="dz-message" ><h2> Click or Drag and Drop files here upload </h2></div>
      </div>
    </template>

    <template slot="clip-uploader-body" slot-scope="props">
      <div class="uploader-files">
        <div class="uploader-file" v-for="file in props.files">

          <div class="file-avatar">
            <img v-bind:src="file.dataUrl" alt="">
          </div>

          <div class="file-details">
            <div class="file-name">
              {{ file.name }}
            </div>

            <div class="file-progress" v-if="file.status !== 'error' && file.status !== 'success'">
              <span class="progress-indicator" v-bind:style="{width: file.progress + '%'}"></span>
            </div>

            <div class="file-meta" v-else>
              <span class="file-size">{{ file.size }}</span>
              <span class="file-status">{{ file.status }}</span>
            </div>
          </div>

          <button :class="buttonClick" @click="buttonClassSwitch" >
              <div class='icon'>
                <i class="far fa-trash-alt"></i>
                <i class="far fa-question-circle"></i>
                <i class="far fa-check-circle"></i>
              </div>
              <div class='text'>
                <span v-if="buttonStatus == 0">Delete</span>
              </div>
            </button>

        </div>
      </div>
    </template>
  </vue-clip>
</template>

<script>
export default {
  data () {
    return {
      options: {
        url: '/upload',
        paramName: 'file',
        acceptedFiles: {
          extensions: ['image/*'],
          message: 'You are uploading an invalid file'
        }
      },
      files: [],
      buttonStatus: 0
    }
  },
  methods: {
    fileAdded(file) {
      this.files.push(file)
    },
    buttonClassSwitch() {
      this.buttonStatus++
      this.buttonStatus = this.buttonStatus % 3
    }  
  },
  computed: {
    buttonClick () {
      return {
        remove: (this.buttonStatus == 0),
        confirm: (this.buttonStatus == 1),
        done: (this.buttonStatus  == 2)
      }
    }
  }
};
</script>

<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  background: #e8e8e8;
  font-family: "Open Sans", sans-serif;
}

.uploader {
  width: 100%;
  height: 100%;
  display: flex;
  border-radius: 6px;
  box-shadow: 1px 2px 19px rgba(195, 195, 195, 0.678);
  flex-direction: column-reverse;
  background: #fff;
}

.uploader * {
  box-sizing: border-box;
}

.uploader-action {
  padding: 20px;
  background: #f1f5ff;
  cursor: pointer;
}

.uploader-action .dz-message {
  color: #94a7c2;
  text-align: center;
  padding: 20px 40px;
  border: 3px dashed #dfe8fe;
  border-radius: 4px;
  font-size: 16px;
}

.uploader-files {
  min-height: 35rem;
  flex: 1;
  padding: 40px;
}

.uploader-file {
  display: grid;
  grid-template-columns: 30% 50% 20%;
}

.file-details {
  display: grid;
  grid-template-rows: 50% auto;
  align-items: center;
}

.uploader-file.upload .file-name {
  color: inherit;
}

.file-progress {
  background: #e3ebfa;
  border-radius: 8px;
  height: 4px;
  width: 80%;
}

.progress-indicator {
  display: block;
  background: #00d28a;
  border-radius: 8px;
  height: 5px;
}

.file-size {
  font-weight: 600;
  color: #bebfc1;
}

.file-status {
  font-size: 12px;
  text-transform: uppercase;
  margin-left: 5px;
}

.uploader-action.dragging {
  background: rgb(0, 255, 128);
  transition: background 300ms ease;
}

@keyframes slideUpIn {
  0% {
    opacity: 0;
    transform: translateY(10%);
  }

  100% {
    opacity: 0;
    transform: none;
  }
}

button {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  cursor: pointer;
  border: 0;
  background: transparent;
  outline: 0;
  overflow: hidden;
}
button .icon {
  position: relative;
  background:#1D242B;
  line-height: 30px;
  width: 30px;
  height: 30px;
  text-align: center;
  color: rgb(255, 255, 255);
  font-size: 18px;
  -webkit-transition: 0.2s color;
  transition: 0.2s color;
  border-radius: 2px;
}
button .icon .fa {
  width: 30px;
  -webkit-transition: 0.2s all;
  transition: 0.2s all;
}
button .icon .fa-check {
  color: #38b87c;
}
button .icon .fa-question {
  color: #2492ff;
}
button .icon:after {
  content: " ";
  display: block;
  position: absolute;
  width: 5px;
  height: 5px;
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  background: #1d242b;
  top: 12.5px;
  right: 1px;
  -webkit-transition: 0.2s right;
  transition: 0.2s right;
  z-index: 1;
}
button .text {
  position: relative;
  width: 0;
  height: 30px;
  overflow: hidden;
  font-family: "Roboto", sans-serif;
  background: #f34541;
  text-align: center;
  line-height: 30px;
  color: #fff;
  font-weight: 300;
  -webkit-transition: 0.2s all;
  transition: 0.2s all;
  border-top-right-radius: 2px;
  border-bottom-right-radius: 2px;
}
button .text span {
  width: 100%;
  opacity: 0;
  position: absolute;
  top: -30px;
  left: 50%;
  -webkit-transform: translateX(-50%);
  transform: translateX(-50%);
  -webkit-transition: 0.3s all;
  transition: 0.3s all;
}
button:hover .icon {
  color: #f34541;
  border-radius: 0;
  border-top-left-radius: 2px;
  border-bottom-left-radius: 2px;
}
button:hover .icon:after {
  right: -2px;
}
button:hover .text {
  width: 120px;
}
button:hover .text span {
  opacity: 1;
  top: 0;
}
button.confirm .icon {
  border-radius: 0;
  border-top-left-radius: 2px;
  border-bottom-left-radius: 2px;
}
button.confirm .icon .fa {
  -webkit-transform: translateY(-30px);
  transform: translateY(-30px);
}
button.confirm .icon:after {
  right: -2px;
}
button.confirm .text {
  background: #2492ff;
  width: 120px;
}
button.confirm .text span {
  opacity: 1;
  top: 0;
}
button.done .icon {
  border-radius: 0;
  border-top-left-radius: 2px;
  border-bottom-left-radius: 2px;
}
button.done .icon .fa {
  -webkit-transform: translateY(-60px);
  transform: translateY(-60px);
}
button.done .icon:after {
  right: -2px;
}
button.done .text {
  background: #38b87c;
  width: 120px;
}
button.done .text span {
  opacity: 1;
  top: 0;
}

@-webkit-keyframes fadeInZoom {
  0% {
    opacity: 0;
    -webkit-transform: scale(0.7);
    transform: scale(0.7);
  }
  100% {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}

@keyframes fadeInZoom {
  0% {
    opacity: 0;
    -webkit-transform: scale(0.7);
    transform: scale(0.7);
  }
  100% {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}
</style>