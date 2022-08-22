# Streamlit

```commandline
streamlit run app.py
```
If you encounter an error like this:
```commandline
OSError: [Errno 24] inotify instance limit reached
```
Use this command instead:
```commandline
streamlit run app.py --server.fileWatcherType None
```

# WebUI access

Open your browser and go to http://localhost:8501
