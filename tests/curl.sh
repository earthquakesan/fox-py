#!/bin/bash
curl -d @$1 -H "Content-Type:application/json; charset=utf-8" http://fox.cs.uni-paderborn.de:4444/fox
