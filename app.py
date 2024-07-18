# import streamlit as st
# from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
# import av
# import cv2


# class VideoTransformer(VideoTransformerBase):
#     def transform(self, frame):
#         img = frame.to_ndarray(format="bgr24")
#         # You can process the image here if needed
#         return av.VideoFrame.from_ndarray(img, format="bgr24")


# st.title("Real-time Camera Feed")

# webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("Real-time Camera Feed")

webrtc_streamer(key="example")
