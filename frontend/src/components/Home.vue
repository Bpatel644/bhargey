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
      files: []
    }
  },
  methods: {
    fileAdded (file) {
      this.files.push(file)
    }
  }
}
</script>

<style>
  body {
    display: flex;
    justify-content: center;
    align-items: center;
    background: #e8e8e8;
    font-family: 'Open Sans', sans-serif;
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
    flex: 1;
    padding: 40px;
  }

  .uploader-file {
    display: grid;
    grid-template-columns: 30% 70%;
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
</style>