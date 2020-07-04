FROM ubuntu:focal
COPY ./ /app/terminator/

EXPOSE 8888

CMD ["/bin/bash"]
