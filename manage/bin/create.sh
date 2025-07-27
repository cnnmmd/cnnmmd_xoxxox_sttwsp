#!/bin/bash

pthtop="$(cd "$(dirname "${0}")/../../../.." && pwd)"
source "${pthtop}"/manage/lib/params.sh
source "${pthtop}"/manage/lib/shared.sh
source "${pthcrr}"/params.sh

pthapp="${pthsrc}"/appwsp
test -d "${pthapp}" || mkdir "${pthapp}"
cd "${pthapp}" && test -d wsp || mkdir wsp
addimg ${imgtgt} "${cnfimg}" "${pthdoc}"
