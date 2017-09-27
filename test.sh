#!/bin/bash
set +eux

check_deps()
{
        if !hash cppcheck 2>/dev/null; then
               echo "Please install cppchecki"
        fi
}

build_babel()
{
        cores=$(grep -c ^processor /proc/cpuinfo)
        make clean
        make -j $cores
}

run_lint()
{
        cppcheck --force . > /dev/null
        echo "Linting successful"
}

run_integration_tests()
{
        pushd tests
                sudo bash ./multihop-basic.sh &
                wait
        popd
}

check_deps
build_babel
run_lint
run_integration_tests
